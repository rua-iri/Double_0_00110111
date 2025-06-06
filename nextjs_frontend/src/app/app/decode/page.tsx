"use client";
import FileUpload from "@/app/components/FileUpload";
import SubmitButton from "@/app/components/SubmitButton";
import { useState } from "react";

export default function Home() {
  const [secretMessage, setSecretMessage] = useState("");

  async function handleFormSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();

    console.log(event.target);
    const formdata = new FormData(event.currentTarget);
    console.log(formdata);

    try {
      const response = await fetch("/api/decodeImage", {
        method: "POST",
        body: formdata,
      });
      const data = await response.json();

      console.log(data);

      setSecretMessage(data.data);
    } catch (error) {
      // TODO: handle this
      console.log(error);
    }
  }

  return (
    <>
      Decode
      <form onSubmit={(event) => handleFormSubmit(event)}>
        <FileUpload />
        <SubmitButton />
      </form>
      <div>
        <p>The secret Message is: {secretMessage}</p>
      </div>
    </>
  );
}
