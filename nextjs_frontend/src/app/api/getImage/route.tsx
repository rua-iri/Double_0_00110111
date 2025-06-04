import { NextRequest } from "next/server";

export async function GET(request: NextRequest) {
  console.log("Decoding image");
  return Response.json({ message: "Hello World" });
}
