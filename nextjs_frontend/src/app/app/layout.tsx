import React from "react";

export default function AppRootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <>
      <div className="flex gap-2.5">
        <a href="/app/encode">Encode</a>
        <a href="/app/decode">Decode</a>
      </div>
      {children}
    </>
  );
}
