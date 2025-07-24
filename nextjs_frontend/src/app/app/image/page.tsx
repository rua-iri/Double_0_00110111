"use client";

// import LoadingIcon from "@/app/components/LoadingIcon";
import PageTitle from "@/app/components/PageTitle";
import Image from "next/image";
import { useSearchParams } from "next/navigation";
import { useEffect, useState } from "react";

export default function Home() {
  const [hasImageLoaded, setHasImageLoaded] = useState(true);
  const [imageURL, setImageURL] = useState("/spy_assets/spy_img_cropped.png");

  const searchParams = useSearchParams();
  const imageId = searchParams.get("id");

  useEffect(() => {
    async function loadImage() {
      try {
        const response = await fetch(`/api/getImage?id=${imageId}`);
        const data = await response.json();

        console.log(data);
        console.log(data.imgData);

        setImageURL(`data:image/png;base64,${data.imgData}`);

        setHasImageLoaded(true);
      } catch (error) {
        // TODO: handle error by displaying a message
        console.error(error);
      }
    }

    loadImage();
  }, [imageId]);

  return (
    <>
      <PageTitle title="Image" />
      {hasImageLoaded ? (
        <div className="flex flex-col">
          <div className="p-3 m-3 border-1 rounded-md bg-white">
            <Image
              width={500}
              height={500}
              src={imageURL}
              alt={"Encoded Image"}
            />
          </div>
          <a
            className="my-1 mx-3 p-3 text-center bg-slate-200 rounded-md hover:bg-slate-300"
            href={imageURL}
            download={`${imageId}_encoded.png`}
          >
            Download Image
          </a>
        </div>
      ) : (
        <div className="p-3 m-3 border-1 rounded-md">
          <p>Image Not Ready Yet...</p>
          <div className="flex justify-center my-2">
            <span className="loader"></span>
          </div>
          {/* <LoadingIcon /> */}
        </div>
      )}
    </>
  );
}
