//
//  ContentView.swift
//  Nutrisync
//
//  Created by Scott MacDonnell on 2024-03-20.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        TabView {
            TodayView()
                .tabItem {
                    Label("Today", systemImage: "chart.bar.doc.horizontal")
                }
            MealsView()
                .tabItem {
                    Label("Meals", systemImage: "fork.knife.circle")
                }
            SettingsView()
                .tabItem {
                    Label("Settings", systemImage: "gear")
                }
        }
    }
}

#Preview {
    ContentView()
}
