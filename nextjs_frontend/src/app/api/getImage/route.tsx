import { NextRequest, NextResponse } from "next/server";

export async function GET(request: NextRequest) {
  try {
    console.log(request);
    console.log(request.nextUrl.searchParams.get("id"));
    const imgId = request.nextUrl.searchParams.get("id");

    if (!imgId) {
      throw new Error("No image ID provided");
    }

    const imgBase64 = await getImageContent(imgId);

    console.log(imgBase64);

    console.log("Decoding image");
    return NextResponse.json({
      status: 200,
      body: {
        imgData: imgBase64,
      },
    });
  } catch (error) {
    if (error instanceof NotFoundError) {
      return NextResponse.json({
        status: 404,
        error: "Image not found",
      });
    }

    return NextResponse.json({
      status: 500,
      error: "Something went wrong",
    });
  }
}

async function getImageContent(imgID: string) {
  const endpointURL: string = `${process.env.BASE_BACKEND_URL}/image/${imgID}`;

  const response = await fetch(endpointURL);
  console.log(response);
  console.log(response.body);

  if (response.status == 202) {
    // TODO: retry request here
  }

  if (response.status == 404) {
    throw new NotFoundError();
  }

  const arrayBuffer = await response.arrayBuffer();
  const buffer = Buffer.from(arrayBuffer);
  return buffer.toString("base64");
}

class NotFoundError extends Error {
  constructor(message: string = "File not found") {
    super(message);
    this.name = "NotFoundError";
  }
}
