type TopSecretLabelProps = {
  labelMessage: string;
};

export default function TopSecretLabel({ labelMessage }: TopSecretLabelProps) {
  return (
    <div className="absolute m-auto left-0 -right-0 text-center -rotate-45 z-10">
      <h1 className="text-5xl text-red-500 opacity-35">{labelMessage}</h1>
    </div>
  );
}
