import React from 'react';

export interface RevOpsMeetingEmbedProps {
  /**
   * Title text above the Calendly widget. Defaults to "Book a Free Systems Audit".
   */
  title?: string;
  /**
   * Subtitle / description below the CTA heading.
   */
  subtitle?: string;
  /**
   * Calendly scheduling URL. Defaults to 'https://calendly.com/renzo-francesqui'
   */
  calendlyUrl?: string;
  /**
   * Locale: 'en' | 'it'. Defaults to 'en'.
   */
  locale?: 'en' | 'it';
}

/**
 * RevOpsMeetingEmbed
 * 
 * Requirement 5: RevOps Meeting Embed
 * Glassmorphic container holding an embedded Calendly iframe booking widget,
 * styled to match the dark futuristic space theme of the portfolio.
 * Heading: "Book a Free Systems Audit" (EN) / "Prenota un Audit Gratuito dei Sistemi" (IT).
 */
export function RevOpsMeetingEmbed({
  title,
  subtitle,
  calendlyUrl = 'https://calendly.com/renzo-francesqui',
  locale = 'en',
}: RevOpsMeetingEmbedProps) {
  const isIt = locale === 'it';
  const ctaHeading = title || (isIt ? 'Prenota un Audit Gratuito dei Sistemi' : 'Book a Free Systems Audit');
  const ctaSubtitle =
    subtitle ||
    (isIt
      ? 'Pianifica una sessione conoscitiva diretta di 30 minuti su architettura revenue e sistemi. Seleziona un orario per analizzare CRM, tracciamento o colli di bottiglia della tua pipeline.'
      : 'Schedule a 30-minute direct revenue architecture & systems discovery session. Select a time on the calendar below to audit your CRM, tracking, or pipeline bottlenecks.');

  const statusText = isIt ? 'Disponibilità in Tempo Reale' : 'Live Scheduling Available';
  const durationText = isIt ? '⏱ Audit Gratuito (30 Min)' : '⏱ Free Systems Audit (30 Min)';

  // Embed URL styled with brand parameters matching the dark space theme
  const embedSrc = `${calendlyUrl}?hide_landing_page_details=1&hide_gdpr_banner=1&background_color=07060a&text_color=f8fafc&primary_color=d4a863`;

  return (
    <section className="card-panel meeting-embed-section" id="meeting-embed">
      <div id="contact-form" />
      <div className="section-header-block">
        <h2 className="section-header-title">
          <span>📅</span> {ctaHeading}
        </h2>
        <p className="section-header-desc">{ctaSubtitle}</p>
      </div>

      {/* Glassmorphic Calendly Iframe Embed Container */}
      <div className="calendly-embed-container" id="calendlyBookingContainer">
        <div className="calendly-widget-header">
          <div className="calendly-status-indicator">
            <span className="pulse-dot" />
            <span className="status-text">{statusText}</span>
          </div>
          <span className="duration-badge">{durationText}</span>
        </div>
        <div className="calendly-inline-widget-wrap">
          <iframe
            src={embedSrc}
            title={ctaHeading}
            loading="lazy"
            className="calendly-iframe"
            width="100%"
            height="700"
            frameBorder="0"
          />
        </div>
      </div>

      {/* Alternative direct communication channels */}
      <div className="contact-channel-pills">
        <a
          href="mailto:renzo.francesqui@gmail.com?subject=Direct%20Inquiry%20regarding%20Systems%20Audit"
          className="channel-pill-link"
        >
          <span>✉️</span> {isIt ? 'Invia Email Diretta' : 'Transmit Direct Email'}
        </a>
        <a
          href="https://www.linkedin.com/in/renzo-francesqui/"
          target="_blank"
          rel="noopener noreferrer"
          className="channel-pill-link"
        >
          <span>💼</span> {isIt ? 'Connettiti su LinkedIn' : 'Connect on LinkedIn'}
        </a>
        <a
          href="/RenzoFrancesquiCV2026.pdf"
          target="_blank"
          download
          className="channel-pill-link"
        >
          <span>📄</span> {isIt ? 'Scarica CV Verificato (PDF)' : 'Download Verified CV (PDF)'}
        </a>
      </div>
    </section>
  );
}

export default RevOpsMeetingEmbed;
