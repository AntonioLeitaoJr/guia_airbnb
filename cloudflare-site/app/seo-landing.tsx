import { ArrowLeft, ArrowUpRight, Check, MapPin } from "lucide-react";
import Image from "next/image";
import Link from "next/link";

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
        <Link className="brand" href="/" aria-label="Voltar ao TE904">
          <Image className="brand-logo" src="/te904-logo.jpeg" alt="Símbolo TE904 da Torre Evidence" width={52} height={52} priority />
          <span><strong>TORRE EVIDENCE</strong><small>APARTAMENTO 904</small></span>
        </Link>
        <Link className="seo-back" href="/"><ArrowLeft /> Voltar ao guia completo</Link>
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
            <Link className="seo-secondary-action" href="/#fotos">Conhecer o apartamento</Link>
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
        <Link href={relatedHref}>Ler o guia <ArrowUpRight /></Link>
      </aside>

      <footer className="seo-page-footer">
        <span>TE904 · Apartamento 904 na Torre Evidence</span>
        <Link href="/">Guia, fotos, estrutura e contato</Link>
      </footer>
    </main>
  );
}
