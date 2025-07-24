type PageTitleProps = {
  title: string;
};

export default function PageTitle({ title }: PageTitleProps) {
  return (
    <div className="mx-3 my-3">
      <h1 className="text-xl font-bold">{title}</h1>
    </div>
  );
}
