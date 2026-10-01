import { GuestGuide } from "./guest-guide";
import Link from "next/link";

export default function Home() {
  return (
    <>
      <GuestGuide />
      <aside className="search-guides" aria-labelledby="search-guides-title">
        <div>
          <span>Conheça melhor o TE904</span>
          <h2 id="search-guides-title">Hospedagem em Belém, no bairro de Nazaré.</h2>
          <p>Veja informações objetivas sobre o Apartamento 904, a Torre Evidence e a localização para planejar sua estadia.</p>
        </div>
        <nav aria-label="Guias sobre a hospedagem">
          <Link href="/hospedagem-em-belem">Hospedagem em Belém</Link>
          <Link href="/apartamento-em-nazare-belem">Apartamento em Nazaré</Link>
        </nav>
      </aside>
    </>
  );
}
