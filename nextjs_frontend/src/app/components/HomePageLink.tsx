type HomePageLinkProps = {
  linkText: string;
  linkURL: string;
};

export default function HomePageLink({ linkText, linkURL }: HomePageLinkProps) {
  return (
    <a
      className="text-xl p-1 hover:bg-[#0000005F] z-20"
      href={linkURL}
      rel="noopener noreferrer"
    >
      {linkText}
    </a>
  );
}
