"use client";

import { FormEvent, useState } from "react";
import {
  ArrowUpRight,
  Building2,
  CalendarDays,
  Camera,
  CarFront,
  Check,
  Clock3,
  Languages,
  MapPinned,
  MessageCircle,
  Send,
  ShieldCheck,
  Sparkles,
  Star,
  WashingMachine,
  Waves,
  Wifi,
} from "lucide-react";
import { toast } from "sonner";

import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from "@/components/ui/accordion";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { NativeSelect, NativeSelectOption } from "@/components/ui/native-select";
import { Textarea } from "@/components/ui/textarea";
import { Toaster } from "@/components/ui/sonner";
import { EventsSection } from "./events-section";
import { PropertyShowcase } from "./property-showcase";

type Language = "pt" | "en" | "es";

const copy = {
  pt: {
    language: "Idioma",
    nav: ["Início", "Guia", "Fotos", "Mapa", "Eventos", "Avaliação"],
    eyebrow: "Seu guia digital em Belém",
    title: "Bem-vindo ao Apartamento 904.",
    intro: "Tudo o que você precisa para uma estadia tranquila, segura e memorável na Torre Evidence.",
    address: "Nazaré · Belém, Pará",
    wifi: "Wi-Fi",
    network: "Rede",
    wifiPrivate: "A senha é informada diretamente ao hóspede no check-in.",
    checkin: "Check-in",
    checkinValue: "A partir das 14h",
    checkout: "Check-out",
    checkoutValue: "Até às 11h",
    emergency: "Precisa de ajuda?",
    emergencyText: "Fale diretamente com o anfitrião por WhatsApp ou ligação.",
    whatsapp: "Chamar no WhatsApp",
    guideEyebrow: "Tudo no lugar certo",
    guideTitle: "Guia do apartamento e do condomínio",
    guideIntro: "Consulte horários, regras e instruções práticas sem precisar procurar em mensagens antigas.",
    guide: {
      lounge: "Lazer · Andar lounge",
      loungeItems: [
        "Piscina, hidromassagem e sauna: das 8h às 18h. Para hidro e sauna, solicite na portaria.",
        "Academia: 24 horas. Controles do ar-condicionado e da TV ficam na portaria.",
        "Quadra infantil e playground: 24 horas. À noite, peça ao porteiro para ligar as luzes da quadra.",
        "Sala de reuniões, churrasqueira, salão de festas e espaço gourmet são pagos à parte e devem ser reservados na portaria.",
      ],
      parking: "Estacionamento · G1",
      parkingItems: [
        "Use a vaga 63.",
        "Não há ponto de recarga para veículo elétrico. O uso das tomadas da garagem é proibido e pode gerar multa.",
      ],
      laundry: "Lavanderia e cobertura",
      laundryItems: [
        "Lavanderia no G3: aberta 24 horas. Se estiver fechada, solicite a chave na portaria.",
        "Pista de cooper na cobertura: das 6h às 18h. Os demais espaços funcionam 24 horas.",
      ],
      stay: "Durante a estadia",
      stayItems: [
        "Silêncio entre 22h e 7h.",
        "Para falar com a portaria, pressione a tecla 1 no interfone.",
        "Desligue o ar-condicionado sempre que sair.",
        "A TV aceita os principais aplicativos de streaming; use a sua própria conta.",
        "Visitas precisam de aviso prévio. Pernoite de visitantes tem taxa adicional paga antecipadamente.",
        "Limpeza durante a estadia é opcional e paga diretamente à prestadora.",
      ],
    },
    cityEyebrow: "Perto de tudo",
    cityTitle: "Explore Belém a partir de Nazaré",
    cityIntro: "O apartamento fica em uma região central, com acesso fácil a serviços, gastronomia e aos principais pontos da cidade.",
    openMap: "Abrir rota no Google Maps",
    places: [
      ["Basílica de Nazaré", "Fé, arquitetura e o coração do Círio"],
      ["Museu Emílio Goeldi", "Natureza e ciência amazônica"],
      ["Estação das Docas", "Gastronomia à beira da Baía do Guajará"],
      ["Ver-o-Peso", "Sabores, cores e cultura paraense"],
    ],
    surveyEyebrow: "Sua experiência importa",
    surveyTitle: "Conte como foi sua estadia",
    surveyIntro: "Leva menos de dois minutos e ajuda a tornar cada nova hospedagem ainda melhor.",
    enjoyed: "Você gostou da hospedagem?",
    recommend: "Recomendaria o apartamento?",
    yes: "Sim",
    no: "Não",
    booking: "Como você reservou?",
    choose: "Selecione uma opção",
    channels: ["Airbnb", "Booking", "Direto com o anfitrião", "Outro"],
    highlight: "O que você mais gostou?",
    improvement: "O que podemos melhorar?",
    name: "Seu nome ou perfil",
    message: "Mensagem final (opcional)",
    submit: "Enviar avaliação",
    submitting: "Enviando...",
    success: "Obrigado! Sua avaliação foi registrada.",
    error: "Não foi possível enviar agora. Seus dados continuam no formulário; tente novamente.",
    required: "Preencha os campos obrigatórios.",
    privacy: "Usaremos sua resposta apenas para melhorar a hospedagem.",
    footer: "Apartamento 904 · Torre Evidence",
    host: "Contato do anfitrião",
  },
  en: {
    language: "Language",
    nav: ["Home", "Guide", "Photos", "Map", "Events", "Review"],
    eyebrow: "Your digital guide to Belém",
    title: "Welcome to Apartment 904.",
    intro: "Everything you need for a calm, safe and memorable stay at Torre Evidence.",
    address: "Nazaré · Belém, Pará",
    wifi: "Wi-Fi",
    network: "Network",
    wifiPrivate: "The password is shared directly with guests at check-in.",
    checkin: "Check-in",
    checkinValue: "From 2 PM",
    checkout: "Check-out",
    checkoutValue: "By 11 AM",
    emergency: "Need help?",
    emergencyText: "Contact your host directly by WhatsApp or phone.",
    whatsapp: "Open WhatsApp",
    guideEyebrow: "Everything in one place",
    guideTitle: "Apartment and condominium guide",
    guideIntro: "Check hours, rules and practical instructions without searching through old messages.",
    guide: {
      lounge: "Leisure · Lounge floor",
      loungeItems: [
        "Pool, hot tub and sauna: 8 AM to 6 PM. Ask the front desk for the hot tub and sauna.",
        "Gym: open 24 hours. Air conditioning and TV controls are available at the front desk.",
        "Children's court and playground: open 24 hours. Ask the doorman to turn on the court lights at night.",
        "Meeting room, barbecue area, party room and gourmet hall are paid separately and must be booked at the front desk.",
      ],
      parking: "Parking · G1",
      parkingItems: [
        "Use parking space 63.",
        "There is no EV charger. Using garage outlets is prohibited and may result in a fine.",
      ],
      laundry: "Laundry and rooftop",
      laundryItems: [
        "Laundry room on G3: open 24 hours. If locked, ask the front desk for the key.",
        "Rooftop jogging track: 6 AM to 6 PM. Other rooftop areas are open 24 hours.",
      ],
      stay: "During your stay",
      stayItems: [
        "Quiet hours are from 10 PM to 7 AM.",
        "Press 1 on the intercom to reach the front desk.",
        "Turn off the air conditioning whenever you leave.",
        "The TV supports major streaming apps; use your own account.",
        "Visitors require prior notice. Overnight guests incur an additional fee paid in advance.",
        "Cleaning during your stay is optional and paid directly to the service provider.",
      ],
    },
    cityEyebrow: "Close to everything",
    cityTitle: "Explore Belém from Nazaré",
    cityIntro: "The apartment is in a central area with easy access to services, local food and the city's main attractions.",
    openMap: "Open route in Google Maps",
    places: [
      ["Basilica of Nazaré", "Faith, architecture and the heart of Círio"],
      ["Emílio Goeldi Museum", "Amazonian nature and science"],
      ["Estação das Docas", "Food and views by Guajará Bay"],
      ["Ver-o-Peso", "Flavors, colors and Pará culture"],
    ],
    surveyEyebrow: "Your experience matters",
    surveyTitle: "Tell us about your stay",
    surveyIntro: "It takes less than two minutes and helps make every future stay even better.",
    enjoyed: "Did you enjoy your stay?",
    recommend: "Would you recommend the apartment?",
    yes: "Yes",
    no: "No",
    booking: "How did you book?",
    choose: "Choose an option",
    channels: ["Airbnb", "Booking", "Direct with the host", "Other"],
    highlight: "What did you enjoy most?",
    improvement: "What could we improve?",
    name: "Your name or profile",
    message: "Final message (optional)",
    submit: "Send review",
    submitting: "Sending...",
    success: "Thank you! Your review was recorded.",
    error: "We could not send it right now. Your answers remain in the form; please try again.",
    required: "Please complete the required fields.",
    privacy: "We will use your response only to improve the stay.",
    footer: "Apartment 904 · Torre Evidence",
    host: "Host contact",
  },
  es: {
    language: "Idioma",
    nav: ["Inicio", "Guía", "Fotos", "Mapa", "Eventos", "Evaluación"],
    eyebrow: "Tu guía digital en Belém",
    title: "Bienvenido al Apartamento 904.",
    intro: "Todo lo que necesitas para una estadía tranquila, segura y memorable en Torre Evidence.",
    address: "Nazaré · Belém, Pará",
    wifi: "Wi-Fi",
    network: "Red",
    wifiPrivate: "La contraseña se comparte directamente con el huésped al hacer el check-in.",
    checkin: "Check-in",
    checkinValue: "Desde las 14:00",
    checkout: "Check-out",
    checkoutValue: "Hasta las 11:00",
    emergency: "¿Necesitas ayuda?",
    emergencyText: "Habla directamente con el anfitrión por WhatsApp o teléfono.",
    whatsapp: "Abrir WhatsApp",
    guideEyebrow: "Todo en un solo lugar",
    guideTitle: "Guía del apartamento y del condominio",
    guideIntro: "Consulta horarios, reglas e instrucciones prácticas sin buscar en mensajes antiguos.",
    guide: {
      lounge: "Ocio · Piso lounge",
      loungeItems: [
        "Piscina, hidromasaje y sauna: de 8:00 a 18:00. Solicita el hidromasaje y la sauna en recepción.",
        "Gimnasio: abierto 24 horas. Los controles del aire acondicionado y la TV están en recepción.",
        "Cancha infantil y parque: abiertos 24 horas. Pide al portero que encienda las luces de la cancha por la noche.",
        "Sala de reuniones, parrilla, salón de fiestas y espacio gourmet se pagan aparte y deben reservarse en recepción.",
      ],
      parking: "Estacionamiento · G1",
      parkingItems: [
        "Utiliza el espacio 63.",
        "No hay cargador para vehículos eléctricos. Usar los enchufes del garaje está prohibido y puede generar una multa.",
      ],
      laundry: "Lavandería y azotea",
      laundryItems: [
        "Lavandería en G3: abierta 24 horas. Si está cerrada, solicita la llave en recepción.",
        "Pista de correr en la azotea: de 6:00 a 18:00. Las demás áreas están abiertas 24 horas.",
      ],
      stay: "Durante la estadía",
      stayItems: [
        "Silencio de 22:00 a 7:00.",
        "Pulsa 1 en el interfono para comunicarte con recepción.",
        "Apaga el aire acondicionado siempre que salgas.",
        "La TV admite las principales aplicaciones de streaming; utiliza tu propia cuenta.",
        "Las visitas requieren aviso previo. Las pernoctas tienen una tarifa adicional pagada por adelantado.",
        "La limpieza durante la estadía es opcional y se paga directamente a la prestadora.",
      ],
    },
    cityEyebrow: "Cerca de todo",
    cityTitle: "Explora Belém desde Nazaré",
    cityIntro: "El apartamento está en una zona céntrica, con fácil acceso a servicios, gastronomía y los principales puntos de la ciudad.",
    openMap: "Abrir ruta en Google Maps",
    places: [
      ["Basílica de Nazaré", "Fe, arquitectura y el corazón del Círio"],
      ["Museo Emílio Goeldi", "Naturaleza y ciencia amazónica"],
      ["Estação das Docas", "Gastronomía junto a la Bahía de Guajará"],
      ["Ver-o-Peso", "Sabores, colores y cultura de Pará"],
    ],
    surveyEyebrow: "Tu experiencia importa",
    surveyTitle: "Cuéntanos cómo fue tu estadía",
    surveyIntro: "Toma menos de dos minutos y ayuda a mejorar cada nueva hospedaje.",
    enjoyed: "¿Te gustó la estadía?",
    recommend: "¿Recomendarías el apartamento?",
    yes: "Sí",
    no: "No",
    booking: "¿Cómo hiciste la reserva?",
    choose: "Selecciona una opción",
    channels: ["Airbnb", "Booking", "Directo con el anfitrión", "Otro"],
    highlight: "¿Qué fue lo que más te gustó?",
    improvement: "¿Qué podemos mejorar?",
    name: "Tu nombre o perfil",
    message: "Mensaje final (opcional)",
    submit: "Enviar evaluación",
    submitting: "Enviando...",
    success: "¡Gracias! Tu evaluación fue registrada.",
    error: "No fue posible enviarla ahora. Tus respuestas siguen en el formulario; inténtalo de nuevo.",
    required: "Completa los campos obligatorios.",
    privacy: "Usaremos tu respuesta solo para mejorar la estadía.",
    footer: "Apartamento 904 · Torre Evidence",
    host: "Contacto del anfitrión",
  },
} as const;

const sectionIds = ["inicio", "guia", "hospedagem", "mapa", "eventos", "avaliacao"];
const placeQueries = ["Basílica de Nazaré Belém", "Museu Emílio Goeldi Belém", "Estação das Docas Belém", "Mercado Ver-o-Peso Belém"];

function SectionHeading({ eyebrow, title, intro }: { eyebrow: string; title: string; intro: string }) {
  return (
    <div className="section-heading">
      <span>{eyebrow}</span>
      <h2>{title}</h2>
      <p>{intro}</p>
    </div>
  );
}

export function GuestGuide() {
  const [language, setLanguage] = useState<Language>("pt");
  const [submitting, setSubmitting] = useState(false);
  const [submitted, setSubmitted] = useState(false);
  const t = copy[language];

  const guideSections = [
    { value: "lounge", icon: Waves, title: t.guide.lounge, items: t.guide.loungeItems },
    { value: "parking", icon: CarFront, title: t.guide.parking, items: t.guide.parkingItems },
    { value: "laundry", icon: WashingMachine, title: t.guide.laundry, items: t.guide.laundryItems },
    { value: "stay", icon: ShieldCheck, title: t.guide.stay, items: t.guide.stayItems },
  ];
  const mobileNavItems = [
    { icon: ShieldCheck, index: 1 },
    { icon: Camera, index: 2 },
    { icon: MapPinned, index: 3 },
    { icon: CalendarDays, index: 4 },
    { icon: Star, index: 5 },
  ];

  async function submitFeedback(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const form = event.currentTarget;
    const data = new FormData(form);
    if (!data.get("enjoyedStay") || !data.get("wouldRecommend") || !data.get("bookingChannel") || !String(data.get("guestName") || "").trim()) {
      toast.error(t.required);
      return;
    }

    setSubmitting(true);
    try {
      const response = await fetch("/api/feedback", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({ language, ...Object.fromEntries(data.entries()) }),
      });
      if (!response.ok) throw new Error("feedback failed");
      setSubmitted(true);
      form.reset();
      toast.success(t.success);
    } catch {
      toast.error(t.error);
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <main>
      <Toaster position="top-center" richColors />
      <header className="topbar">
        <a className="brand" href="#inicio" aria-label="Torre Evidence 904">
          <span className="brand-mark">E</span>
          <span><strong>TORRE EVIDENCE</strong><small>APARTAMENTO 904</small></span>
        </a>
        <nav className="desktop-nav" aria-label="Navegação principal">
          {t.nav.map((label, index) => <a key={label} href={`#${sectionIds[index]}`}>{label}</a>)}
        </nav>
        <label className="language-control">
          <Languages aria-hidden="true" />
          <span className="sr-only">{t.language}</span>
          <select value={language} onChange={(event) => setLanguage(event.target.value as Language)} aria-label={t.language}>
            <option value="pt">PT</option>
            <option value="en">EN</option>
            <option value="es">ES</option>
          </select>
        </label>
      </header>

      <section className="hero" id="inicio">
        <img src="/torre-evidence.jpg" alt="Fachada iluminada da Torre Evidence à noite" />
        <div className="hero-overlay" />
        <div className="hero-content">
          <span className="eyebrow"><Sparkles /> {t.eyebrow}</span>
          <h1>{t.title}</h1>
          <p>{t.intro}</p>
          <span className="address"><MapPinned /> {t.address}</span>
        </div>
      </section>

      <section className="quick-grid" aria-label="Informações rápidas">
        <article className="quick-card wifi-card">
          <div className="quick-icon"><Wifi /></div>
          <div className="quick-copy">
            <span className="card-label">{t.wifi}</span>
            <strong>{t.network}: TE904</strong>
            <p>{t.wifiPrivate}</p>
          </div>
        </article>
        <article className="quick-card time-card">
          <div className="quick-icon"><Clock3 /></div>
          <div><span className="card-label">{t.checkin}</span><strong>{t.checkinValue}</strong></div>
          <div className="time-divider" />
          <div><span className="card-label">{t.checkout}</span><strong>{t.checkoutValue}</strong></div>
        </article>
        <article className="quick-card help-card">
          <div className="quick-icon"><MessageCircle /></div>
          <div><span className="card-label">{t.emergency}</span><p>{t.emergencyText}</p></div>
          <Button asChild className="whatsapp-button"><a href="https://api.whatsapp.com/send?phone=5591988241288">{t.whatsapp}<ArrowUpRight /></a></Button>
        </article>
      </section>

      <section className="content-section guide-section" id="guia">
        <SectionHeading eyebrow={t.guideEyebrow} title={t.guideTitle} intro={t.guideIntro} />
        <div className="guide-layout">
          <div className="guide-aside">
            <div className="guide-aside-icon"><Building2 /></div>
            <p>Torre Evidence</p>
            <strong>Av. Alcindo Cacela, 2304</strong>
            <span>Nazaré · Belém</span>
          </div>
          <Accordion type="multiple" defaultValue={["lounge", "stay"]} className="guide-accordion">
            {guideSections.map(({ value, icon: Icon, title, items }) => (
              <AccordionItem value={value} key={value}>
                <AccordionTrigger><span className="accordion-title"><Icon />{title}</span></AccordionTrigger>
                <AccordionContent>
                  <ul>{items.map((item) => <li key={item}><Check /> <span>{item}</span></li>)}</ul>
                </AccordionContent>
              </AccordionItem>
            ))}
          </Accordion>
        </div>
      </section>

      <PropertyShowcase language={language} />

      <section className="city-section" id="mapa">
        <div className="city-inner">
          <SectionHeading eyebrow={t.cityEyebrow} title={t.cityTitle} intro={t.cityIntro} />
          <div className="map-shell">
            <iframe title="Mapa de pontos de interesse próximos à Torre Evidence" src="https://www.google.com/maps/d/u/0/embed?mid=1ZvQHCJBfEfJSD6iFA0f8zVFVM5aZ5_k&ehbc=2E312F" loading="lazy" />
            <a className="map-link" href="https://www.google.com/maps/search/?api=1&query=Av.+Alcindo+Cacela,+2304,+Belém,+PA" target="_blank" rel="noreferrer"><MapPinned /> {t.openMap}<ArrowUpRight /></a>
          </div>
          <div className="places-grid">
            {t.places.map(([name, description], index) => (
              <a key={name} href={`https://www.google.com/maps/search/?api=1&query=${encodeURIComponent(placeQueries[index])}`} target="_blank" rel="noreferrer">
                <span>0{index + 1}</span><div><strong>{name}</strong><p>{description}</p></div><ArrowUpRight />
              </a>
            ))}
          </div>
        </div>
      </section>

      <EventsSection language={language} />

      <section className="content-section survey-section" id="avaliacao">
        <SectionHeading eyebrow={t.surveyEyebrow} title={t.surveyTitle} intro={t.surveyIntro} />
        <form className="survey-form" onSubmit={submitFeedback}>
          <div className="choice-row">
            <fieldset>
              <legend>{t.enjoyed} *</legend>
              <label><input type="radio" name="enjoyedStay" value="yes" /><span>{t.yes}</span></label>
              <label><input type="radio" name="enjoyedStay" value="no" /><span>{t.no}</span></label>
            </fieldset>
            <fieldset>
              <legend>{t.recommend} *</legend>
              <label><input type="radio" name="wouldRecommend" value="yes" /><span>{t.yes}</span></label>
              <label><input type="radio" name="wouldRecommend" value="no" /><span>{t.no}</span></label>
            </fieldset>
          </div>
          <label className="field-label">{t.booking} *
            <NativeSelect name="bookingChannel" defaultValue="" className="field-control" required>
              <NativeSelectOption value="" disabled>{t.choose}</NativeSelectOption>
              {t.channels.map((channel) => <NativeSelectOption key={channel} value={channel}>{channel}</NativeSelectOption>)}
            </NativeSelect>
          </label>
          <div className="field-grid">
            <label className="field-label">{t.highlight}<Textarea name="highlight" rows={4} maxLength={800} /></label>
            <label className="field-label">{t.improvement}<Textarea name="improvement" rows={4} maxLength={800} /></label>
          </div>
          <label className="field-label">{t.name} *<Input name="guestName" maxLength={120} required /></label>
          <label className="field-label">{t.message}<Textarea name="finalMessage" rows={4} maxLength={1200} /></label>
          <div className="submit-row">
            <p><ShieldCheck /> {t.privacy}</p>
            <Button type="submit" disabled={submitting || submitted} size="lg" className="submit-button">
              {submitted ? <><Check /> {t.success}</> : submitting ? t.submitting : <><Send /> {t.submit}</>}
            </Button>
          </div>
        </form>
      </section>

      <footer>
        <div className="brand footer-brand"><span className="brand-mark">E</span><span><strong>{t.footer}</strong><small>Belém · Pará</small></span></div>
        <a href="https://api.whatsapp.com/send?phone=5591988241288"><MessageCircle /> {t.host}</a>
      </footer>

      <nav className="mobile-nav" aria-label="Navegação móvel">
        {mobileNavItems.map(({ icon: Icon, index }) => <a href={`#${sectionIds[index]}`} key={sectionIds[index]}><Icon /><span>{t.nav[index]}</span></a>)}
      </nav>
    </main>
  );
}
