import Link from "next/link"

import { cn } from "@/lib/utils"

type SidebarItem = {
  href: string
  label: string
}

type SidebarProps = {
  items?: SidebarItem[]
  className?: string
}

const defaultItems: SidebarItem[] = [
  { href: "/dashboard", label: "Overview" },
  { href: "/dashboard/activity", label: "Activity" },
  { href: "/dashboard/team", label: "Team" },
  { href: "/dashboard/settings", label: "Settings" },
]

export function Sidebar({ items = defaultItems, className }: SidebarProps) {
  return (
    <aside className={cn("h-full w-64 border-r bg-muted/30 p-3", className)}>
      <nav className="grid gap-1">
        {items.map((item) => (
          <Link
            key={item.href}
            href={item.href}
            className="rounded-md px-3 py-2 text-sm text-muted-foreground transition-colors hover:bg-muted hover:text-foreground"
          >
            {item.label}
          </Link>
        ))}
      </nav>
    </aside>
  )
}
