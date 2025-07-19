"use client";

import LoadingIcon from "@/app/components/LoadingIcon";
import Image from "next/image";
import { useSearchParams } from "next/navigation";
import { useEffect, useState } from "react";

export default function Home() {
  const [hasImageLoaded, setHasImageLoaded] = useState(false);
  const [imageURL, setImageURL] = useState("/file.svg");

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
      <h1 className="text-lg">Image</h1>
      {hasImageLoaded ? (
        <>
          <div className="p-3 m-3 border-1 rounded-md">
            <Image
              width={500}
              height={500}
              src={imageURL}
              alt={"Encoded Image"}
            />
          </div>
          <a
            className="p-3 bg-amber-200 rounded-md hover:bg-amber-600 cursor-pointer"
            href={imageURL}
            download={`${imageId}_encoded.png`}
          >
            Download Image
          </a>
        </>
      ) : (
        <div className="p-3 m-3 border-1 rounded-md">
          <p>Image Not Ready Yet...</p>
          <div className="flex justify-center my-2">
            {/* <span className="loader"></span> */}
          </div>
          <LoadingIcon />
        </div>
      )}
    </>
  );
}
