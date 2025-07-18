export default function TextInput() {
  return (
    <div className="outline-1 outline-slate-900 rounded-md py-5 px-3 m-3">
      <label className="block" htmlFor="message">
        Enter your secret message
      </label>
      <input
        className="block outline-1 outline-slate-900 rounded-md p-1"
        type="text"
        name="message"
        id="message"
        required
      />
    </div>
  );
}
