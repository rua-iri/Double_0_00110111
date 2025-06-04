import { NextRequest } from "next/server";

export async function GET(request: NextRequest) {
  const endpoint: string = `${process.env.BASE_BACKEND_URL}/image/`;
  console.log(request);
  console.log("Decoding image");
  return Response.json({ message: "Hello World" });
}
