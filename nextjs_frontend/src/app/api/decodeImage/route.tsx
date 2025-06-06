import { NextRequest, NextResponse } from "next/server";

export async function POST(request: NextRequest) {
  const endpointURL: string = `${process.env.BASE_BACKEND_URL}/decode`;
  console.log("Decoding image");
  const formData = await request.formData();

  try {
    const response = await fetch(endpointURL, {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    console.log(response);
    console.log(data);

    if (response.status == 400) {
      return NextResponse.json({ error: "Image not encoded" }, { status: 400 });
    }

    return NextResponse.json({
      status: 200,
      data: data.message,
    });
  } catch (error) {
    console.log(error);
    return NextResponse.json(
      { error: "Something went wrong" },
      { status: 500 }
    );
  }
}
