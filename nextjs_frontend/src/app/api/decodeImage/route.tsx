import { NextRequest } from "next/server";

export async function POST(request: NextRequest) {
  console.log("Decoding image");
  return Response.json({ message: "Hello World" });
}
