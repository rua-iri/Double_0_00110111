import { NextRequest } from "next/server";

export async function GET(request: NextRequest) {
  const url = request.nextUrl;
  console.log(url);
  return Response.json({ message: "Hello World" });
}


