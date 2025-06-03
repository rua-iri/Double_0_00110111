export default function UploadFile() {
  return (
    <div className="outline-1 outline-slate-900 rounded-md p-5">
      <input className="hidden" type="file" name="fileInput" id="fileInput" />
      <label
        className="bg-slate-900 hover:bg-slate-700 text-white p-3 rounded-md"
        htmlFor="fileInput"
      >
        Select File
      </label>
    </div>
  );
}
