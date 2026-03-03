package main

import (
	"fmt"
	"os"
	"path/filepath"
	"strings"

	"github.com/happyhackingspace/vt/pkg/template"
)

func main() {
	repoPath := "../.."
	if len(os.Args) > 1 {
		repoPath = os.Args[1]
	}

	absPath, err := filepath.Abs(repoPath)
	if err != nil {
		panic(fmt.Sprintf("error resolving path: %v", err))
	}

	entries, err := os.ReadDir(absPath)
	if err != nil {
		panic(fmt.Sprintf("error reading directory: %v", err))
	}

	for _, entry := range entries {
		if strings.HasPrefix(entry.Name(), ".") || !entry.IsDir() {
			continue
		}
		validateCategory(filepath.Join(absPath, entry.Name()), entry.Name())
	}
}

func validateCategory(categoryPath, categoryName string) {
	err := filepath.WalkDir(categoryPath, func(path string, d os.DirEntry, err error) error {
		if err != nil {
			return err
		}
		if path == categoryPath {
			return nil
		}
		if strings.HasPrefix(d.Name(), ".") {
			if d.IsDir() {
				return filepath.SkipDir
			}
			return nil
		}
		if !d.IsDir() {
			return nil
		}

		indexPath := filepath.Join(path, "index.yaml")
		if _, statErr := os.Stat(indexPath); statErr != nil {
			return nil
		}

		if _, loadErr := template.LoadTemplate(path); loadErr != nil {
			panic(fmt.Sprintf("[%s/%s] %v", categoryName, d.Name(), loadErr))
		}

		return filepath.SkipDir
	})

	if err != nil {
		panic(fmt.Sprintf("error scanning %s: %v", categoryName, err))
	}
}
