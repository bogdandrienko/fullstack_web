import * as navbar from "./navbar";
import * as footer from "./footer";

export function Base1({ title, children }: any) {
  return (
    <div>
      <navbar.Navbar1>{title}</navbar.Navbar1>
      <main>{children}</main>
      <footer.Footer1 />
    </div>
  );
}
