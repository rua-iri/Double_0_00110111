import { NextRequest, NextResponse } from "next/server";

export async function GET(request: NextRequest) {
  try {
    console.log(request.nextUrl.searchParams.get("id"));
    const imgId = request.nextUrl.searchParams.get("id");

    if (!imgId) {
      throw new NotFoundError("No image ID provided");
    }

    const imgBase64 = await getImageContent(imgId);

    console.log("Decoding image");
    return NextResponse.json({
      status: 200,
        imgData: imgBase64,
    });
  } catch (error) {
    if (error instanceof NotFoundError) {
      return NextResponse.json({ error: "Image not found" }, { status: 404 });
    }

    console.log(error);

    return NextResponse.json(
      { error: "Something went wrong" },
      { status: 500 }
    );
  }
}

async function getImageContent(imgID: string) {
  const endpointURL: string = `${process.env.BASE_BACKEND_URL}/image/${imgID}`;

  const response = await requestImage(endpointURL);

  if (response.status == 404) {
    throw new NotFoundError();
  }

  if (response.status >= 500) {
    throw new Error();
  }

  const arrayBuffer = await response.arrayBuffer();
  const buffer = Buffer.from(arrayBuffer);
  return buffer.toString("base64");
}

async function requestImage(endpointURL: string) {
  const timeoutInterval = 1500;
  const maxAttempts = 5;
  let attemptCount = 0;

  while (attemptCount < maxAttempts) {
    const response = await fetch(endpointURL);
    console.log(response.status);

    if (response.status != 202) {
      return response;
    }

    console.log(`Current Attempt Count: ${attemptCount}`);
    attemptCount++;

    await new Promise((resolve) => setTimeout(resolve, timeoutInterval));
  }

  throw new Error("Request timed out");
}

class NotFoundError extends Error {
  constructor(message: string = "File not found") {
    super(message);
    this.name = "NotFoundError";
  }
}
