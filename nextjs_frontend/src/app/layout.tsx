import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import NavigationTab from "./components/NavigationTab";
import PageFooter from "./components/PageFooter";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Double_0_00110111",
  description: "Online Steganography Service",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        <div className="grid grid-cols-12 gap-0 mx-32 my-15">
          <div className="manilla-file col-span-6 shadow-lg/30 bg-white">
            {children}
            <PageFooter />
          </div>
          <div className="my-3 flex flex-col gap-0.5">
            <NavigationTab tabText="HOME" tabLink="/" />
            <NavigationTab tabText="ENCODE" tabLink="/app/encode" />
            <NavigationTab tabText="DECODE" tabLink="/app/decode" />
          </div>
        </div>
      </body>
    </html>
  );
}
