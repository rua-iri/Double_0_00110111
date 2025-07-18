import Image from "next/image";
import HomePageLink from "./components/HomePageLink";
import TopSecretLabel from "./components/TopSecretLabel";

export default function Home() {
  return (
    <div className="manilla-file bg-white mx-32 my-15">
      <main className="pb-12 relative">
        <div className="grid grid-cols-2">
          <div className="px-5">
            <Image
              className="grayscale p-1 bg-white shadow-lg/30"
              src={"/goldeneye_assets/testimg.jpg"}
              alt={"Secret Agent Photo"}
              width={300}
              height={600}
            />
          </div>
          <div className="flex flex-col items-end gap-5 px-15 py-5">
            <Image
              className="grayscale mix-blend-multiply"
              src={
                "/goldeneye_assets/Coat_of_arms_of_the_United_Kingdom_sm.png"
              }
              alt={"UK Coat of Arms"}
              width={200}
              height={100}
            />
            <h1 className="text-xl" title="Yes, it's seven in binary">
              Double_0_00110111
            </h1>
          </div>
        </div>

        <div className="flex flex-col items-center my-20 py-5 gap-5 relative">
          <HomePageLink linkText={"1. ENCODE"} linkURL={"/app/encode"} />
          <HomePageLink linkText={"2. DECODE"} linkURL={"/app/decode"} />
          <TopSecretLabel labelMessage="FOR YOUR EYES ONLY" />
        </div>
      </main>
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
    </div>
  );
}
