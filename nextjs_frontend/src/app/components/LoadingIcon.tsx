export default function LoadingIcon() {
  return (
    <div className="bg-black rounded-full h-48 w-48 flex justify-center items-center">
      <div className="h-44 w-44 relative flex justify-center items-center">
        <div className="absolute top-0 left-0 w-5 h-5 bg-yellow-500 translate-y-35 translate-x-10 rotate-50"></div>
        <div className="absolute top-0 left-0 w-5 h-5 bg-yellow-600 translate-y-30 translate-x-6 rotate-60"></div>
        <div className="absolute top-0 left-0 w-5 h-5 bg-orange-400 translate-y-25 translate-x-3 rotate-70"></div>
        <div className="absolute top-0 left-0 w-5 h-5 bg-orange-500 translate-y-20 translate-x-0 rotate-90"></div>
        <div className="absolute top-0 left-0 w-5 h-5 bg-orange-600 translate-y-15 translate-x-0 rotate-90"></div>
        <div className="absolute top-0 left-0 w-5 h-5 bg-red-500 translate-y-10 translate-x-3 rotate-100"></div>
        <div className="absolute top-0 left-0 w-5 h-5 bg-red-600 translate-y-5 translate-x-6 rotate-110"></div>
        <div className="absolute top-0 left-0 w-5 h-5 bg-red-700 translate-y-0 translate-x-10 rotate-120"></div>

        <div className="w-32 h-32 rounded-full bg-green-900 opacity-75"></div>

        <div className="absolute top-0 left-0 w-5 h-5 bg-blue-100 translate-y-35 translate-x-30 rotate-120"></div>
        <div className="absolute top-0 left-0 w-5 h-5 bg-blue-200 translate-y-30 translate-x-33 rotate-110"></div>
        <div className="absolute top-0 left-0 w-5 h-5 bg-blue-300 translate-y-25 translate-x-36 rotate-100"></div>
        <div className="absolute top-0 left-0 w-5 h-5 bg-blue-400 translate-y-20 translate-x-40 rotate-90"></div>
        <div className="absolute top-0 left-0 w-5 h-5 bg-blue-500 translate-y-15 translate-x-40 rotate-90"></div>
        <div className="absolute top-0 left-0 w-5 h-5 bg-blue-600 translate-y-10 translate-x-36 rotate-80"></div>
        <div className="absolute top-0 left-0 w-5 h-5 bg-blue-700 translate-y-5 translate-x-33 rotate-70"></div>
        <div className="absolute top-0 left-0 w-5 h-5 bg-blue-800 translate-y-0 translate-x-30 rotate-60"></div>
      </div>
    </div>
  );
}
