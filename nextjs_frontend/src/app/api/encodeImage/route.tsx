import { NextRequest, NextResponse } from "next/server";

export async function POST(request: NextRequest) {
  const endpointURL: string = `${process.env.BASE_BACKEND_URL}/encode`;

  console.log("Encoding image");
  // console.log(request);

  const formData = await request.formData();

  // send user request to backend
  try {
    const response = await fetch(endpointURL, {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    console.log(data);

    return NextResponse.json({
      status: 200,
      data: data,
    });
  } catch (error) {
    console.log(error);
    return NextResponse.json(
      { error: "Something went wrong" },
      { status: 500 }
    );
  }
}
