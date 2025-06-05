import { NextRequest } from "next/server";

export async function GET(request: NextRequest) {
  let endpointURL: string = `${process.env.BASE_BACKEND_URL}/image/`;

  try {
    console.log(request);
    console.log(request.nextUrl.searchParams.get("id"));
    const imgId = request.nextUrl.searchParams.get("id");
    endpointURL += imgId;

    const response = await fetch(endpointURL);
    console.log(response);
    console.log(response.body);
    const arrayBuffer = await response.arrayBuffer();
    const buffer = Buffer.from(arrayBuffer);
    const imgBase64 = buffer.toString("base64");

    console.log("Decoding image");
    return Response.json({
      status: "success",
      imgData: imgBase64,
    });
  } catch (error) {
    console.log(error);
  }
}
