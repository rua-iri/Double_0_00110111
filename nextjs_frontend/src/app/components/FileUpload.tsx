import React, { useState } from "react";

export default function UploadFile() {
  const [filename, setFilename] = useState("");

  return (
    <div className="outline-1 outline-slate-900 rounded-md p-5">
      <input
        className="hidden"
        type="file"
        name="fileInput"
        id="fileInput"
        onChange={(event: React.FormEvent<HTMLInputElement>) => {
          setFilename(event.currentTarget.value);
          console.log(event.currentTarget);
        }}
      />
      <label
        className="bg-slate-900 hover:bg-slate-700 text-white p-3 rounded-md cursor-pointer"
        htmlFor="fileInput"
      >
        Select File
      </label>
      <p className="m-5 w-10 text-xs">{filename}</p>
    </div>
  );
}
