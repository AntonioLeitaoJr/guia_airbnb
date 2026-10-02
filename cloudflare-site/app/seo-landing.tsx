/* eslint-disable @next/next/no-html-link-for-pages -- Full document navigation is intentional: Vinext client routing does not reliably leave these SEO routes in embedded mobile browsers. */
import { ArrowLeft, ArrowUpRight, Check, MapPin } from "lucide-react";
import Image from "next/image";

const bookingUrl = "https://www.booking.com/hotel/br/apartamento-no-coracao-da-amazonia.pt-br.html";

type SeoSection = {
  heading: string;
  paragraphs: readonly string[];
  points?: readonly string[];
};

type SeoLandingProps = {
  eyebrow: string;
  title: string;
  intro: string;
  image: string;
  imageAlt: string;
  sections: readonly SeoSection[];
  relatedHref: string;
  relatedTitle: string;
  relatedDescription: string;
};

export function SeoLanding({
  eyebrow,
  title,
  intro,
  image,
  imageAlt,
  sections,
  relatedHref,
  relatedTitle,
  relatedDescription,
}: SeoLandingProps) {
  return (
    <main className="seo-page">
      <header className="seo-topbar">
        <a className="brand" href="/" aria-label="Voltar ao TE904">
          <Image className="brand-logo" src="/te904-logo.jpeg" alt="Símbolo TE904 da Torre Evidence" width={52} height={52} priority />
          <span><strong>TORRE EVIDENCE</strong><small>APARTAMENTO 904</small></span>
        </a>
        <a className="seo-back" href="/"><ArrowLeft /> Voltar ao guia completo</a>
      </header>

      <section className="seo-landing-hero">
        <div className="seo-landing-copy">
          <span>{eyebrow}</span>
          <h1>{title}</h1>
          <p>{intro}</p>
          <div className="seo-landing-actions">
            <a className="seo-primary-action" href={bookingUrl} target="_blank" rel="noopener noreferrer">
              Ver disponibilidade na Booking.com <ArrowUpRight />
            </a>
            <a className="seo-secondary-action" href="/#fotos">Conhecer o apartamento</a>
          </div>
        </div>
        <figure>
          <Image src={image} alt={imageAlt} fill sizes="(max-width: 980px) 100vw, 46vw" priority />
          <figcaption><MapPin /> Nazaré · Belém · Pará</figcaption>
        </figure>
      </section>

      <article className="seo-article">
        {sections.map((section) => (
          <section key={section.heading}>
            <h2>{section.heading}</h2>
            {section.paragraphs.map((paragraph) => <p key={paragraph}>{paragraph}</p>)}
            {section.points && (
              <ul>
                {section.points.map((point) => <li key={point}><Check /> <span>{point}</span></li>)}
              </ul>
            )}
          </section>
        ))}
      </article>

      <aside className="seo-related" aria-label="Conteúdo relacionado">
        <div>
          <span>Continue planejando</span>
          <h2>{relatedTitle}</h2>
          <p>{relatedDescription}</p>
        </div>
        <a href={relatedHref}>Ler o guia <ArrowUpRight /></a>
      </aside>

      <footer className="seo-page-footer">
        <span>TE904 · Apartamento 904 na Torre Evidence</span>
        <a href="/">Guia, fotos, estrutura e contato</a>
      </footer>
    </main>
  );
}
