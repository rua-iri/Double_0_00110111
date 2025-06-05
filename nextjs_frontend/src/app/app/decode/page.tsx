"use client";
import FileUpload from "@/app/components/FileUpload";
import SubmitButton from "@/app/components/SubmitButton";

export default function Home() {
  function handleFormSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();

    console.log(event.target);
    const formdata = new FormData(event.currentTarget);
    console.log(formdata);
  }

  return (
    <>
      Decode
      <form onSubmit={(event) => handleFormSubmit(event)}>
        <FileUpload />
        <SubmitButton />
      </form>
    </>
  );
}
