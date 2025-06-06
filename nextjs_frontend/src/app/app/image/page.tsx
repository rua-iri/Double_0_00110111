"use client";

import Image from "next/image";
import { useSearchParams } from "next/navigation";
import { useEffect, useState } from "react";

export default function Home() {
  const [hasImageLoaded, setHasImageLoaded] = useState(false);
  const [imageURL, setImageURL] = useState("/file.svg");

  const searchParams = useSearchParams();
  const id = searchParams.get("id");

  async function loadImage() {
    try {
      const response = await fetch(`/api/getImage?id=${id}`);
      const data = await response.json();

      console.log(data);
      console.log(data.imgData);

      setImageURL(`data:image/gif;base64,${data.imgData}`);

      setHasImageLoaded(true);
    } catch (error) {
      // TODO: handle error by displaying a message
      console.error(error);
    }
  }

  useEffect(() => {
    loadImage();
  }, [id]);

  return (
    <>
      Image
      {hasImageLoaded ? (
        <Image width={500} height={500} src={imageURL} alt={"Encoded Image"} />
      ) : (
        <div>Image Not Ready</div>
      )}
    </>
  );
}
