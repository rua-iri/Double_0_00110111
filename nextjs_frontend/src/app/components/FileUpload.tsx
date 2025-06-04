import React, { useState } from "react";

export default function UploadFile() {
  const [filename, setFilename] = useState("C:\\fakepath\\filename.png");

  return (
    <div className="outline-1 outline-slate-900 rounded-md py-5 px-3 my-3">
      <div>
        <input
          className="max-h-0 max-w-0"
          type="file"
          name="fileInput"
          id="fileInput"
          onChange={(event: React.FormEvent<HTMLInputElement>) => {
            setFilename(event.currentTarget.value);
            console.log(event.currentTarget);
          }}
          required
        />
        <label
          className="bg-slate-900 hover:bg-slate-700 text-white p-2 rounded-md cursor-pointer"
          htmlFor="fileInput"
          tabIndex={0}
        >
          Select File
        </label>
      </div>
      <div className="my-3">
        <code>
          <pre className="bg-gray-300 w-44 overflow-scroll noScrollbar rounded-md">
            {filename}
          </pre>
        </code>
      </div>
    </div>
  );
}
