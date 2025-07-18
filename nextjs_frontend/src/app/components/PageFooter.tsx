import Image from "next/image";

export default function PageFooter() {
  return (
    <footer className="mt-30 row-start-3 flex gap-[24px] flex-wrap items-center justify-center">
      <a
        className="flex items-center gap-2 hover:underline hover:underline-offset-4"
        href="https://rua-iri.com"
        target="_blank"
        rel="noopener noreferrer"
      >
        <Image
          aria-hidden
          src="/globe.svg"
          alt="Globe icon"
          width={16}
          height={16}
        />
        rua-iri.com
      </a>
      <a
        href="https://github.com/rua-iri/Double_0_00110111/"
        className="flex items-center gap-2 hover:underline hover:underline-offset-4"
        target="_blank"
        rel="noopener noreferrer"
      >
        <Image
          src="/GitHub_Invertocat_Dark.svg"
          width={16}
          height={16}
          alt="GitHub Logo"
        />
        Source Code
      </a>
    </footer>
  );
}
