import Image from "next/image";

export default function Home() {
  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className="flex flex-col gap-[32px] row-start-2 items-center sm:items-start">
        <h1 className="text-3xl font-[family-name:var(--font-geist-mono)]" title="Yes, it's seven in binary">
          Double_0_00110111
        </h1>

        <div className="flex gap-4 items-center flex-col sm:flex-row">
          <a
            className="rounded-full border border-solid border-transparent transition-colors flex items-center justify-center bg-foreground text-background gap-2 hover:bg-[#383838] dark:hover:bg-[#ccc] font-medium text-sm sm:text-base h-10 sm:h-12 px-4 sm:px-5 sm:w-auto"
            href="/encode"
            rel="noopener noreferrer"
          >
            <Image
              className="dark:invert"
              src="/import-content.svg"
              alt="Vercel logomark"
              width={20}
              height={20}
            />
            Encode
          </a>
          <a
            className="rounded-full border border-solid border-transparent transition-colors flex items-center justify-center bg-foreground text-background gap-2 hover:bg-[#383838] dark:hover:bg-[#ccc] font-medium text-sm sm:text-base h-10 sm:h-12 px-4 sm:px-5 sm:w-auto"
            href="/decode"
            rel="noopener noreferrer"
          >
            <Image
              className="dark:invert"
              src="/export-content.svg"
              alt="Vercel logomark"
              width={20}
              height={20}
            />
            Decode
          </a>
        </div>
      </main>
      <footer className="row-start-3 flex gap-[24px] flex-wrap items-center justify-center">
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
    </div>
  );
}
