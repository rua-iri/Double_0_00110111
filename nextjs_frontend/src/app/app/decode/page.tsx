"use client";
import FileUpload from "@/app/components/FileUpload";
import PageTitle from "@/app/components/PageTitle";
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
      <PageTitle title="Decode Image" />
      {isFormSubmitted ? (
        <div>
          <p>The secret Message is: &quot;{secretMessage}&quot;</p>
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
