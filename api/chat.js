export default async function handler(req, res) {
    // Enable CORS for development testing
    res.setHeader('Access-Control-Allow-Credentials', true);
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,DELETE,POST,PUT');
    res.setHeader(
        'Access-Control-Allow-Headers',
        'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version'
    );

    // Handle OPTIONS request
    if (req.method === 'OPTIONS') {
        return res.status(200).end();
    }

    if (req.method !== 'POST') {
        return res.status(405).json({ error: 'Method Not Allowed' });
    }

    const API_KEY = process.env.GEMINI_API_KEY;
    if (!API_KEY) {
        console.error("GEMINI_API_KEY environment variable is not configured.");
        return res.status(500).json({ error: 'Gemini API key is not configured on the Vercel environment.' });
    }

    try {
        const { contents, systemInstruction } = req.body;

        const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=${API_KEY}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                contents,
                systemInstruction
            })
        });

        if (!response.ok) {
            const errorText = await response.text();
            console.error(`Gemini API error (Status ${response.status}):`, errorText);
            return res.status(response.status).send(errorText);
        }

        const data = await response.json();
        return res.status(200).json(data);

    } catch (err) {
        console.error("Serverless proxy error:", err);
        return res.status(500).json({ error: err.message });
    }
}
