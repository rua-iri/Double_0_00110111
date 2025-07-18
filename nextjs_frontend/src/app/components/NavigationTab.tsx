type NavigationTabProps = {
  tabText: string;
  tabLink: string | undefined;
};

export default function NavigationTab({
  tabText,
  tabLink,
}: NavigationTabProps) {
  return (
    <div className="manilla-file [writing-mode:vertical-lr] h-32 w-8 text-wrap rounded-r-3xl relative">
      <div className="absolute inset-0 bg-amber-900/20 rounded-r-3xl z-10"></div>
      <a className="relative z-20 flex justify-center w-full h-full rounded-r-3xl hover:bg-[#0000005F]" href={tabLink}>
        <p>
        {tabText}
        </p>
      </a>
    </div>
  );
}
