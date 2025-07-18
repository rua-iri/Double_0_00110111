import React, { Suspense } from "react";
import TopSecretLabel from "../components/TopSecretLabel";

export default function AppRootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <main className="pb-12 relative">
      <Suspense>{children}</Suspense>
      <div className="flex flex-col items-center my-20 py-5 gap-5 relative">
        <TopSecretLabel labelMessage="CONFIDENTIAL" />
      </div>
    </main>
  );
}
