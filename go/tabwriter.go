package main

import (
	"io"
	"text/tabwriter"
)

const (
	tabwriterMinWidth = 6
	tabwriterWidth    = 4
	tabwriterPadding  = 3
	tabwriterPadChar  = ' '
)

func NewTabWriter(out io.Writer) *tabwriter.Writer {
	return tabwriter.NewWriter(out, tabwriterMinWidth, tabwriterWidth, tabwriterPadding, tabwriterPadChar, 0)
}
