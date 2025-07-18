import Image from "next/image";
import HomePageLink from "./components/HomePageLink";
import TopSecretLabel from "./components/TopSecretLabel";

export default function Home() {
  return (
    <main className="pb-12 relative">
      <div className="grid grid-cols-2">
        <div className="px-5 relative">
          <Image
            className="grayscale p-1 bg-white shadow-lg/30 select-none"
            src={"/spy_assets/spy_img_cropped.png"}
            alt={"Secret Agent Photo"}
            width={300}
            height={600}
          />
          <Image
            className="absolute -top-2.5 select-none"
            src={"/spy_assets/paperclip.png"}
            alt={"Paperclip"}
            width={75}
            height={75}
          />
        </div>
        <div className="flex flex-col items-end gap-5 px-15 py-5">
          <Image
            className="grayscale mix-blend-multiply select-none"
            src={"/spy_assets/Coat_of_arms_of_the_United_Kingdom_sm.png"}
            alt={"UK Coat of Arms"}
            width={200}
            height={100}
          />
          <h1 className="text-xl font-black" title="Yes, it's seven in binary">
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
  );
}
