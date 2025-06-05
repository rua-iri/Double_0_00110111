"use client";
import FileUpload from "@/app/components/FileUpload";
import SubmitButton from "@/app/components/SubmitButton";
import TextInput from "@/app/components/TextInput";
import { useRouter } from "next/navigation";
import React from "react";

export default function Home() {
  const router = useRouter();

  async function handleFormSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();

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

      const imgPageURL = `/app/image?id=${data.uuid}`;
      router.push(imgPageURL);
    } catch (error) {
      console.log(error);
    }
  }

  return (
    <>
      Encode
      <form onSubmit={(event) => handleFormSubmit(event)}>
        <FileUpload />
        <TextInput />
        <SubmitButton />
      </form>
    </>
  );
}
