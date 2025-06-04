import { NextRequest } from "next/server";

export async function POST(request: NextRequest) {
  const endpoint: string = `${process.env.BASE_BACKEND_URL}/decode`;

  const response = await fetch(endpoint);

  console.log("Decoding image");
  return Response.json({ message: "Hello World" });
}
