import { NextRequest } from "next/server";

export async function POST(request: NextRequest) {
  console.log("Encoding image");
  console.log(request);
  return Response.json({ message: "Hello World" });
}
