"use client";
import FileUpload from "@/app/components/FileUpload";
import React from "react";

export default function Home() {
  function handleFormSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();

    console.log(event.target);
  }

  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className="flex flex-col gap-[32px] row-start-2 items-center sm:items-start">
        Encode
        <form onSubmit={(event) => handleFormSubmit(event)}>
          <FileUpload />
          <input type="submit" value="submit" />
        </form>
      </main>
    </div>
  );
}
