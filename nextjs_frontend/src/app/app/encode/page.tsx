"use client";
import FileUpload from "@/app/components/FileUpload";
import SubmitButton from "@/app/components/SubmitButton";
import TextInput from "@/app/components/TextInput";
import { useRouter } from "next/navigation";
import React, { useState } from "react";

export default function Home() {
  const [isFormSubmitted, setIsFormSubmitted] = useState(false);
  const router = useRouter();

  async function handleFormSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setIsFormSubmitted(true);

    console.log(event.target);
    const formdata = new FormData(event.currentTarget);
    console.log(formdata);

    try {
      const response = await fetch("/api/encodeImage", {
        method: "POST",
        body: formdata,
      });
      const data = await response.json();
      console.log(data);

      const imgPageURL = `/app/image?id=${data.data.uuid}`;
      router.push(imgPageURL);
    } catch (error) {
      // TODO: handle this
      console.log(error);
      setIsFormSubmitted(false);
    }
  }

  return (
    <>
      <h1 className="text-lg">Encode</h1>
      {isFormSubmitted ? (
        <div className="debug my-42"></div>
      ) : (
        <div className="my-14">
          <form onSubmit={(event) => handleFormSubmit(event)}>
            <FileUpload />
            <TextInput />
            <SubmitButton />
          </form>
        </div>
      )}
    </>
  );
}
