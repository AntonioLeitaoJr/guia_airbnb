import {
  AirVent,
  ArrowUpRight,
  CarFront,
  ChefHat,
  Dumbbell,
  MapPin,
  ShieldCheck,
  Sparkles,
  Star,
  Waves,
  WashingMachine,
} from "lucide-react";

type Language = "pt" | "en" | "es";

const bookingUrl = "https://www.booking.com/hotel/br/apartamento-no-coracao-da-amazonia.pt-br.html";

const content = {
  pt: {
    eyebrow: "Conheça cada detalhe",
    title: "Conforto de casa, estrutura completa.",
    intro: "Um studio moderno de 47 m², no coração de Nazaré, preparado para descansar, trabalhar e viver Belém com praticidade.",
    galleryLabel: "Galeria do apartamento e do condomínio",
    facilitiesTitle: "Apartamento e facilidades do prédio",
    facilities: ["Piscina", "Academia 24h", "Estacionamento", "Hidromassagem", "Lavanderia", "Cozinha equipada", "Ar-condicionado", "Portaria 24h"],
    reviewsEyebrow: "Experiência comprovada",
    reviewsTitle: "O que os hóspedes mais valorizam",
    reviewThemes: [
      ["Limpeza impecável", "Organização e cuidado aparecem de forma recorrente nas avaliações."],
      ["Localização excelente", "Fácil acesso à Basílica, ao Museu Goeldi e aos serviços de Nazaré."],
      ["Conforto de verdade", "Ambiente amplo, funcional, bem equipado e fiel às fotos."],
      ["Anfitrião presente", "Orientações claras e atendimento atencioso do início ao fim."],
    ],
    score: "9,7",
    scoreLabel: "Excepcional",
    scoreMeta: "29 avaliações na Booking.com · consultado em set. de 2026",
    privacy: "Comentários apresentados como temas anonimizados, sem nomes ou dados pessoais de hóspedes.",
    booking: "Ver disponibilidade na Booking.com",
  },
  en: {
    eyebrow: "See every detail",
    title: "The comfort of home, with complete amenities.",
    intro: "A modern 47 m² studio in the heart of Nazaré, designed for resting, working and exploring Belém with ease.",
    galleryLabel: "Apartment and building gallery",
    facilitiesTitle: "Apartment and building amenities",
    facilities: ["Pool", "24h gym", "Parking", "Hot tub", "Laundry", "Equipped kitchen", "Air conditioning", "24h front desk"],
    reviewsEyebrow: "A proven experience",
    reviewsTitle: "What guests value most",
    reviewThemes: [
      ["Impeccable cleanliness", "Organization and care are recurring themes in guest feedback."],
      ["Excellent location", "Easy access to the Basilica, Museu Goeldi and Nazaré services."],
      ["Genuine comfort", "A spacious, practical, well-equipped place that matches the photos."],
      ["Attentive host", "Clear guidance and thoughtful support throughout the stay."],
    ],
    score: "9.7",
    scoreLabel: "Exceptional",
    scoreMeta: "29 Booking.com reviews · checked Sep 2026",
    privacy: "Reviews are shown as anonymized themes, without guest names or personal information.",
    booking: "Check availability on Booking.com",
  },
  es: {
    eyebrow: "Conoce cada detalle",
    title: "La comodidad de casa con estructura completa.",
    intro: "Un studio moderno de 47 m² en el corazón de Nazaré, pensado para descansar, trabajar y descubrir Belém con practicidad.",
    galleryLabel: "Galería del apartamento y del edificio",
    facilitiesTitle: "Apartamento y comodidades del edificio",
    facilities: ["Piscina", "Gimnasio 24h", "Estacionamiento", "Hidromasaje", "Lavandería", "Cocina equipada", "Aire acondicionado", "Recepción 24h"],
    reviewsEyebrow: "Experiencia comprobada",
    reviewsTitle: "Lo que más valoran los huéspedes",
    reviewThemes: [
      ["Limpieza impecable", "La organización y el cuidado se repiten en las evaluaciones."],
      ["Ubicación excelente", "Fácil acceso a la Basílica, el Museo Goeldi y los servicios de Nazaré."],
      ["Comodidad real", "Un espacio amplio, funcional, equipado y fiel a las fotos."],
      ["Anfitrión atento", "Orientaciones claras y atención cuidadosa durante toda la estadía."],
    ],
    score: "9,7",
    scoreLabel: "Excepcional",
    scoreMeta: "29 evaluaciones en Booking.com · consultado en sep. de 2026",
    privacy: "Las evaluaciones se presentan como temas anonimizados, sin nombres ni datos personales.",
    booking: "Ver disponibilidad en Booking.com",
  },
} as const;

const photos = [
  ["/apartamento/sala.jpg", "Sala integrada e iluminada do Apartamento 904"],
  ["/apartamento/piscina.jpg", "Piscina da Torre Evidence"],
  ["/apartamento/quarto.jpg", "Cama de casal e área de trabalho"],
  ["/apartamento/cozinha.jpg", "Studio com cozinha e sala integradas"],
  ["/apartamento/cama.jpg", "Quarto preparado para a chegada"],
  ["/apartamento/tv.jpg", "Smart TV e área de estar"],
] as const;

const facilityIcons = [Waves, Dumbbell, CarFront, Sparkles, WashingMachine, ChefHat, AirVent, ShieldCheck];

export function PropertyShowcase({ language }: { language: Language }) {
  const t = content[language];

  return (
    <section className="property-section" id="hospedagem">
      <div className="property-inner">
        <div className="section-heading">
          <span>{t.eyebrow}</span>
          <h2>{t.title}</h2>
          <p>{t.intro}</p>
        </div>

        <div className="photo-gallery" aria-label={t.galleryLabel}>
          {photos.map(([src, alt], index) => <img key={src} src={src} alt={alt} loading={index === 0 ? "eager" : "lazy"} />)}
        </div>

        <div className="facility-panel">
          <div>
            <MapPin />
            <span>Nazaré · Belém</span>
            <strong>{t.facilitiesTitle}</strong>
          </div>
          <ul>
            {t.facilities.map((label, index) => {
              const Icon = facilityIcons[index];
              return <li key={label}><Icon /><span>{label}</span></li>;
            })}
          </ul>
        </div>

        <div className="reviews-layout">
          <div className="score-card">
            <span>Booking.com</span>
            <strong>{t.score}</strong>
            <p><Star /> {t.scoreLabel}</p>
            <small>{t.scoreMeta}</small>
            <a href={bookingUrl}>{t.booking}<ArrowUpRight /></a>
          </div>
          <div className="review-content">
            <span className="review-eyebrow">{t.reviewsEyebrow}</span>
            <h3>{t.reviewsTitle}</h3>
            <div className="review-grid">
              {t.reviewThemes.map(([title, description]) => (
                <article key={title}><Sparkles /><div><strong>{title}</strong><p>{description}</p></div></article>
              ))}
            </div>
            <p className="review-privacy"><ShieldCheck /> {t.privacy}</p>
          </div>
        </div>
      </div>
    </section>
  );
}
