"use client";
import FileUpload from "@/app/components/FileUpload";
import SubmitButton from "@/app/components/SubmitButton";
import { useState } from "react";

export default function Home() {
  const [isFormSubmitted, setIsFormSubmitted] = useState(false);
  const [secretMessage, setSecretMessage] = useState("");

  async function handleFormSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setIsFormSubmitted(true);

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
      setIsFormSubmitted(false);
    }
  }

  return (
    <>
      <h1 className="text-lg">Decode</h1>
      {isFormSubmitted ? (
        <div>
          <p>The secret Message is: "{secretMessage}"</p>
        </div>
      ) : (
        <div>
          <form onSubmit={(event) => handleFormSubmit(event)}>
            <FileUpload />
            <SubmitButton />
          </form>
        </div>
      )}
    </>
  );
}
