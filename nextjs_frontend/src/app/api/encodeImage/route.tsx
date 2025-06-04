import { NextRequest } from "next/server";

export async function POST(request: NextRequest) {
  const endpoint: string = `${process.env.BASE_BACKEND_URL}/decode`;

  console.log("Encoding image");
  console.log(request);
  return Response.json({ message: "Hello World" });
}
