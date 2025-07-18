import React, { Suspense } from "react";
import PageFooter from "../components/PageFooter";
import NavigationTab from "../components/NavigationTab";

export default function AppRootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <main className="pb-12 relative">
      <Suspense>{children}</Suspense>
    </main>
  );
}
