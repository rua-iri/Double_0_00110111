import Image from "next/image";
import HomePageLink from "./components/HomePageLink";
import TopSecretLabel from "./components/TopSecretLabel";
import PageFooter from "./components/PageFooter";
import NavigationTab from "./components/NavigationTab";

export default function Home() {
  return (
    <div className="grid grid-cols-12 gap-0 mx-32 my-15">
      <div className="manilla-file col-span-6 shadow-lg/30 bg-white">
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
              <h1
                className="text-xl font-black"
                title="Yes, it's seven in binary"
              >
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
        <PageFooter />
      </div>
      <div className="my-3 flex flex-col gap-0.5">
        <NavigationTab tabText="" tabLink="#" />
        <NavigationTab tabText="ENCODE" tabLink="/app/encode" />
        <NavigationTab tabText="DECODE" tabLink="/app/decode" />
      </div>
    </div>
  );
}
