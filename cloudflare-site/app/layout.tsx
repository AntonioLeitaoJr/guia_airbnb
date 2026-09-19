import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Guia Torre Evidence | Apartamento 904",
  description:
    "Informações essenciais para uma estadia confortável no Apartamento 904 da Torre Evidence, em Belém.",
  icons: {
    icon: "/favicon.svg",
    shortcut: "/favicon.svg",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="pt-BR">
      <body>{children}</body>
    </html>
  );
}
