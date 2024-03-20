//
//  TodayView.swift
//  Nutrisync
//
//  Created by Scott MacDonnell on 2024-03-20.
//

import SwiftUI

struct TodayView: View {
    let currentDate = Date()
    
    var body: some View {
        ScrollView {
            VStack(alignment: .leading) {
                // Title
                HStack {
                    Text("Today")
                        .font(.largeTitle)
                        .fontWeight(.bold)
                    
                    Spacer()
                }
                
                // Date
                HStack {
                    Text(currentDate, style: .date)
                        .font(.title2)
                        .fontWeight(.semibold)
                        .foregroundColor(.secondary)
                    
                    Spacer()
                }
                .padding(.bottom)
                
            }
            .padding()
        }
    }
}

#Preview {
    TodayView()
}
