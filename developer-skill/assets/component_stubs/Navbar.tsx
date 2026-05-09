import Link from "next/link"

import { cn } from "@/lib/utils"

type NavbarProps = {
  className?: string
}

const navItems = [
  { href: "/dashboard", label: "Dashboard" },
  { href: "/projects", label: "Projects" },
  { href: "/settings", label: "Settings" },
]

export function Navbar({ className }: NavbarProps) {
  return (
    <header className={cn("border-b bg-background", className)}>
      <div className="mx-auto flex h-14 max-w-7xl items-center justify-between px-4">
        <Link href="/" className="font-semibold">
          App
        </Link>
        <nav className="flex items-center gap-4 text-sm text-muted-foreground">
          {navItems.map((item) => (
            <Link key={item.href} href={item.href} className="transition-colors hover:text-foreground">
              {item.label}
            </Link>
          ))}
        </nav>
      </div>
    </header>
  )
}
